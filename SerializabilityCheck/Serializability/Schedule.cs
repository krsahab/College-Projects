using System;
using System.Collections.Generic;
using System.Linq;

namespace Serializability
{
    public class Schedule
    {
        public List<Operation> Schedules { get; set; }
        public HashSet<int> Transactions { get; set; }
        public Schedule(string[] schedule)
        {
            try
            {
                Schedules = new List<Operation>();
                Transactions = new HashSet<int>();
                Populate(schedule);
            }
            catch (Exception e)
            {
                Console.WriteLine("Error occured while parsing Schedules");
                Console.WriteLine("Message: " + e.StackTrace);
            }
        }
        private void Populate(string[] schedule)
        {
            for (int i = 0; i < schedule.Length; i++)
            {
                char action = schedule[i][0];
                int num, ind = 1, transaction = 0;
                while (int.TryParse(schedule[i][ind].ToString(), out num))
                {
                    transaction = transaction * (int)Math.Pow(10, ind - 1) + num;
                    ind++;
                }
                Transactions.Add(transaction);
                char item = schedule[i][schedule[i].Length - 1];
                Schedules.Add(new Operation(action, transaction, item));
            }
        }
        //Create Precedence Graph in the form of Adjecency matrix
        public int[,] CreatePrecedenceGraph()
        {
            int nodes = Transactions.Count;
            int[,] graph = new int[nodes, nodes];
            for (int i = 0; i < Schedules.Count; i++)
                for (int j = i + 1; j < Schedules.Count; j++)
                    if (Schedules[i].Transaction != Schedules[j].Transaction && (Schedules[i].Action == 'w' || Schedules[j].Action == 'w'))
                        graph[Schedules[i].Transaction - 1, Schedules[j].Transaction - 1] = 1;
            return graph;
        }
        //Cycle Detection and Serializability Order using Topological Sorting
        public List<int> CycleDetectionAndSerialOrder(int[,] graph, out bool isCyclic)
        {
            int V = Transactions.Count;
            List<int> TransactionOrder = new List<int>();
            bool[] visited = new bool[V];
            int[] innode = new int[V];
            Queue<int> q = new Queue<int>();
            int count = 0;

            for (int i = 0; i < V; i++)
                for (int j = 0; j < V; j++)
                    if (graph[i, j] == 1)
                        innode[j]++;

            for (int i = 0; i < V; i++)
                if (innode[i] == 0)
                    q.Enqueue(i);

            while (q.Count > 0)
            {
                int t = q.Dequeue();
                TransactionOrder.Add(t);
                for (int i = 0; i < V; i++)
                {
                    if (graph[t, i] == 1)
                    {
                        innode[i]--;
                        if (innode[i] == 0)
                            q.Enqueue(i);
                    }
                }
                count++;
            }
            isCyclic = count != V;
            return TransactionOrder;
        }
        public string GetSchedules()
        {
            string schedule = "";
            foreach (var s in Schedules)
                schedule += s + ", ";
            return schedule;
        }
        public class Operation
        {
            public char Action { get; set; }
            public int Transaction { get; set; }
            public char Item { get; set; }
            public Operation(char action, int transaction, char item)
            {
                Action = action;
                Transaction = transaction;
                Item = item;
            }
            public override string ToString()
            {
                return Action.ToString() + Transaction.ToString() + Item.ToString();
            }
        }
    }
}
