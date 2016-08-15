using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Kata3
{
    class Kata
    {
        public static long NextBiggerNumber(long n)
        {
            string nString = n.ToString();
            StringBuilder resultString = new StringBuilder(nString);

            if (nString.Length > 1)
            {
                int idx = nString.Length - 2;

                do
                {
                    if (nString[idx] < nString[idx + 1])
                    {
                        int nextIndex = idx + 1;
                        string remainder = nString.Substring(nextIndex);

                        if (remainder.Length > 1)
                        {
                            remainder = String.Concat(remainder.OrderBy(c => c));
                            char nextHigher = remainder.Where(c => c > nString[idx]).First();
                            int nextHigherIndex = remainder.IndexOf(nextHigher);

                            resultString[idx] = nextHigher;
                            remainder = remainder.Remove(nextHigherIndex, 1);
                            remainder += nString[idx];
                            remainder = String.Concat(remainder.OrderBy(c => c));

                            resultString.Remove(nextIndex, resultString.Length - nextIndex);
                            resultString.Append(remainder);
                        }
                        else
                        {
                            resultString[idx] = nString[idx + 1];
                            resultString[idx + 1] = nString[idx];
                        }                                           

                        break;
                    }

                    idx--;
                }
                while (idx >= 0);
            }

            long result = Int64.Parse(resultString.ToString());

            return result == n ? -1 : result;
        }
    }
}
