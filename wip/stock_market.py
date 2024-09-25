# https://open.kattis.com/problems/borsen

from dataclasses import dataclass, field
from typing import Self
import random

DEBUG   =   True

@dataclass
class StockMarket:
    n:  int     # N days
    q:  float   # transaction fee Q
    prices: dict[int, float] = field(default_factory=dict, init=True)
    assets: dict[str, float] = field(default_factory=dict, init=False)

    def __post_init__(self) -> None:
        self.assets = {'cash': 100.0, 'stock': 0.0}
        # return self.test_run()
        # return self.monte_carlo(100_000_000)
        return self.run()
    
    def run(self) -> None:

        i = 0
        while self.prices[i + 1] != None:
            print(f"prices[{i}] = {self.prices[i]}", end=' ')
            dp = self.prices[i+1] - self.prices[i]
            if self.assets['cash'] > 0 and dp  * self.assets['cash'] / self.prices[i] - self.q > 0:
                self.buy_stock(self.assets['cash'] - self.q, i)
            elif self.assets['stock'] > 0 and dp * self.assets['stock'] - self.q < 0:
                self.sell_stock(self.assets['stock'], i)
            else:
                print('+'*38, '[hold]')
            print(f"assets = {self.assets}")
            
            i += 1

        print(f"prices[{i}] = {self.prices[i]}", end=' ')
        if self.assets['stock'] > 0:
            self.sell_stock(self.assets['stock'], i)
        print(f"assets = {self.assets}")
        
        return
    
    def monte_carlo(self, n: int) -> None:
        self.max = 0
        while (n:= n - 1) + 1:
            print("*"*50,f'[epoch {n}] max: {self.max}')
            self.assets = {'cash': 100.0, 'stock': 0.0}
            self.epoch()
            if self.assets['cash'] > self.max:
                self.max = self.assets['cash']
        return

    def epoch(self) -> None:
        try:
            for i in range(self.n):
                if i == self.n - 1:
                    self.sell_stock(self.assets['stock'] * self.prices[i], i)
                else:
                    buyamt = random.uniform(-self.assets['stock'] * self.prices[i], self.assets['cash'] - self.q)
                    if buyamt >= 0:
                        self.buy_stock(buyamt, i)
                    else:
                        self.sell_stock(-buyamt, i)

                if DEBUG:
                    print(f"{i} : buy stock amt = {buyamt}")
                    print(f"assets = {self.assets}")
        except ValueError as e:
                print(f'[Error] : {e}')
        return

    def test_run(self) -> None:
        try:
            day = 3
            self.buy_stock(50.0, day)
            if DEBUG:
                print(f"n = {self.n}, q = {self.q}")
                print(f"prices = {self.prices}")
                print(f"assets = {self.assets}")
    
            self.sell_stock(self.assets['stock'], day)
            if DEBUG:
                print(f"n = {self.n}, q = {self.q}")
                print(f"prices = {self.prices}")
                print(f"assets = {self.assets}")
        except ValueError as e:
            print(f'[Error] : {e}')

        return

    def buy_stock(self, amt: float, day: int) -> None:
        if DEBUG:
            print('+'*28, '[buy_stock]')
        if self.assets['cash'] == 0:
            raise ValueError('Cash is zero.')
            return
        elif self.assets['cash'] < amt + self.q:
            raise ValueError('Insufficient cash to transact.')
            return
        else:
            self.assets['cash'] -= amt + self.q
            self.assets['stock'] += round(amt / self.prices[day], 10)
        return 

    def sell_stock(self, stock: float, day: int) -> None:
        if DEBUG:
            print('+'*28, '[sell_stock]')
        if self.assets['stock'] == 0:
            raise ValueError('Stock balance is zero.')
            return
        elif self.assets['stock']  < stock:
            raise ValueError('Insufficient stock balance to sell')
            return
        else:
            self.assets['stock'] -= stock
            self.assets['cash'] += round(stock * self.prices[day] - self.q, 10)
        return 


    @classmethod
    def parse_inputs(cls) -> Self:
        n = int(input().strip())
        q = float(input().strip())
        prices = dict()
        i = -1
        while (i:= i + 1) < n:
            try:
                prices[i] = float(input().strip())
                #if DEBUG:
                #    print(f'prices = {prices}')
            except ValueError as e:
                print(f"Error: {e}")
                return None
        prices[i] = None
        return cls(n=n, q=q, prices=prices)








def main() -> None:

    stockmarket = StockMarket.parse_inputs()
    if DEBUG and stockmarket:
        print('-'*38, '[main]')
        print(f"n = {stockmarket.n}, q = {stockmarket.q}")
        print(f"prices = {stockmarket.prices}")
        print(f"assets = {stockmarket.assets}")
    # print(f"max = {stockmarket.max}")

    return


if __name__ == "__main__":
    main()
