using System;

namespace Serializability
{
    class Program
    {
        public static void Main(string[] args)
        {
            Schedule s;
            if (args.Length > 0)
                s = new Schedule(args);
            else
            {
                string[] schedule = { "r1x", "r2z", "r1z", "r3y", "r3y", "w1x", "w3y", "r2y", "w2z", "w2y" };
                //string[] schedule = { "r1x", "r2z", "r1z", "r3y", "r3y", "w1x" };
                s = new Schedule(schedule);
            }
            Console.WriteLine("-------------------------------------------------------------------------------");
            Console.WriteLine("Schedules: " + s.GetSchedules());

            Console.WriteLine("Precedence Graph: ");
            var precedenceGraph = s.CreatePrecedenceGraph();
            for (int i = 0; i < s.Transactions.Count; i++)
                for (int j = 0; j < s.Transactions.Count; j++)
                    if (precedenceGraph[i, j] == 1)
                        Console.WriteLine((i + 1) + " --> " + (j + 1));

            bool isCyclic = false;
            var serializabilityOrder = s.CycleDetectionAndSerialOrder(precedenceGraph, out isCyclic);
            if (isCyclic)
                Console.WriteLine("Cycle Detected, Given schedule is not Conflict Serializable");
            else
            {
                Console.WriteLine("Given schedule is Conflict Serializable with Equivalent serial order as :");
                foreach (var num in serializabilityOrder) { Console.Write(num + 1 + " "); }
                Console.WriteLine();
            }
            Console.WriteLine("-------------------------------------------------------------------------------");
        }
    }
}
