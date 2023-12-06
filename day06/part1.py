#!/usr/bin/env python3
"""
aoc2021 solution skeleton
"""

import logging
import math
from argparse import ArgumentParser
from pathlib import Path


def main():
    """main"""

    parser = ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    logging.info(args)

    data = Path(args.input).read_text(encoding='utf-8').splitlines()

    times = list(map(int, data[0].split()[1:]))
    distances = list(map(int, data[1].split()[1:]))
    print(times)
    print(distances)

    # times [7, 15, 30]
    # distance [9, 40, 200]

    ans = []
    for idx in range(len(times)):
        wins = 0

        for hold_time in range(times[idx]):
            travel_time = times[idx] - hold_time
            distance = travel_time * hold_time
            if distance > distances[idx]:
                wins += 1

        ans.append(wins)

    print(ans)
    print(f'ans {math.prod(ans)}')

    """
    ## there should be mathematical apparatus to solve this challenge

    speed = hold_time
    speed * (total_time - hold_time) > distance
    hold_time * total_time - hold_time ^ 2 > distance

    total_time = 7, distance = 9
    7x - x^2 > 9


    ## and chatbot to the rescue for high school math

    ```
    Certainly! Let's solve the inequality \(7x - x^2 > 9\).

    1. **Reorder Terms:** Rearrange the inequality so the terms are in descending order of powers of \(x\):
    
       \( -x^2 + 7x > 9\)
    
    2. **Move all terms to one side:**
    
       \( -x^2 + 7x - 9 > 0\)
    
    3. **Factor if possible:** Factoring might help identify critical points.
    
       This inequality doesn't easily factor.
    
    4. **Find Critical Points:** To find where this quadratic is equal to zero, use the quadratic formula: \( x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \).
    
       For \( -x^2 + 7x - 9 > 0 \):
       \( a = -1, b = 7, c = -9 \)
    
       \( x = \frac{-7 \pm \sqrt{7^2 - 4(-1)(-9)}}{2(-1)} \)
       \( x = \frac{-7 \pm \sqrt{49 - 36}}{-2} \)
       \( x = \frac{-7 \pm \sqrt{13}}{-2} \)
    
       So the critical points are \(x = \frac{-7 + \sqrt{13}}{-2}\) and \(x = \frac{-7 - \sqrt{13}}{-2}\).
    
    5. **Test Intervals:** Use test points within intervals created by the critical points to determine where the inequality holds true.
    
       Consider intervals: \((- \infty, \frac{-7 - \sqrt{13}}{-2})\), \((\frac{-7 - \sqrt{13}}{-2}, \frac{-7 + \sqrt{13}}{-2})\), \((\frac{-7 + \sqrt{13}}{-2}, +\infty)\).
    
       Pick a test point from each interval to test the inequality.
    
       - For \(x = 0\): \( -0^2 + 7 \times 0 - 9 > 0\), which simplifies to \(-9 > 0\). This is false.
    
       - For \(x = -3\): \( -(-3)^2 + 7 \times (-3) - 9 > 0\), which simplifies to \(9 - 21 - 9 > 0\), \( -21 > 0\). This is also false.
    
       - For \(x = 3\): \( -3^2 + 7 \times 3 - 9 > 0\), which simplifies to \(-9 + 21 - 9 > 0\), \(3 > 0\). This is true.
    
    6. **Express the Solution Set:** The solution is \( x \in \left(\frac{-7 - \sqrt{13}}{-2}, \frac{-7 + \sqrt{13}}{-2}\right)\).
    ```

    ## finalize

    reorder equation, pull coefficients and solve with quadratic formula

    7x - x^2 > 9

    -x^2 + 7x - 9 > 0
    yields quadratic equation coefficients a=-1, b=7, c=-9

    x = (-1*b +- sqrt(b**2 - 4*a*c)) / 2*a
    compute x1 +
    compute x2 -
    >> check intervals (-inf, x1), (x1, x2), (x2, inf) to find solution
    """

    wins = []
    for idx in range(len(times)):

        a = -1
        b = times[idx]
        c = -1 * distances[idx]

        x1 = (-1*b + math.sqrt(b**2 - 4*a*c)) / 2*a
        x2 = (-1*b - math.sqrt(b**2 - 4*a*c)) / 2*a
        # we skip the inf/-inf range tests as we expect the solution to be
        # x1 < H < x2
        wins.append(math.ceil(x2 - 1) - math.floor(x1 + 1) + 1)

    print(wins)
    print(f'ans math {math.prod(wins)}')


if __name__ == '__main__':
    main()
