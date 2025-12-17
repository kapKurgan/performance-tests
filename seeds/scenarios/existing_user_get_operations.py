# Цель — реализовать сидинг, который будет создавать 300 пользователей, открывать для каждого пользователя
# кредитный счёт, а затем выполнять для каждого пользователя следующее:
# 5 операций покупки.
# 1 операция пополнения счёта.
# 1 операция снятия наличных.

from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan, SeedOperationsPlan


class ExistingUserGetOperationsSeedsScenario(SeedsScenario):
    @property
    def plan(self) -> SeedsPlan:
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,
                credit_card_accounts=SeedAccountsPlan(
                    count=1,
                    top_up_operations=SeedOperationsPlan(count=1),
                    purchase_operations=SeedOperationsPlan(count=5),
                    cash_withdrawal_operations=SeedOperationsPlan(count=1),
                )
            )
        )

    @property
    def scenario(self) -> str:
        return "existing_user_get_operations"


if __name__ == '__main__':
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()
