import asyncio

# Функция силач
async def start_strongman(name, power):
    print(f'Силач {name} начал соревнование')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i} гирю')
    print(f'Силач {name} заклнчил соревнование')

# Функция соревнование
async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Denis', 4))
    task2 = asyncio.create_task(start_strongman('Pasha', 3))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3

# Запуск соревнования
asyncio.run(start_tournament())
