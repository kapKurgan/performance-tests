from abc import ABC, abstractmethod

from seeds.builder import build_grpc_seeds_builder
from seeds.dumps import save_seeds_result, load_seeds_result
from seeds.schema.plan import SeedsPlan
from seeds.schema.result import SeedsResult
from tools.logger import get_logger

logger = get_logger("SEEDS_SCENARIO")
class SeedsScenario(ABC):
    """ Абстрактный класс для работы со сценариями сидинга.
        Этот класс инкапсулирует общую логику генерации, сохранения и загрузки данных для тестов. """

    def __init__(self):
        """ Инициализация класса SeedsScenario.
            Создаёт экземпляр билдера для генерации сидинговых данных через gRPC. """
        self.builder = build_grpc_seeds_builder()

    @property
    @abstractmethod
    def plan(self) -> SeedsPlan:
        """ Абстрактное свойство для получения плана сидинга.
            Должно быть переопределено в дочерних классах. """
        ...

    @property
    @abstractmethod
    def scenario(self) -> str:
        """ Абстрактное свойство для получения имени сценария сидинга.
            Должно быть переопределено в дочерних классах. """
        ...

    def save(self, result: SeedsResult) -> None:
        """ Сохраняет результат сидинга в файл.
            :param result: Объект SeedsResult, содержащий сгенерированные данные. """
        logger.info(f"[{self.scenario}] Сохраняем результаты сидинга в файл")
        save_seeds_result(result=result, scenario=self.scenario)
        logger.info(f"[{self.scenario}] Результат сидинга в файл сохранен успешно")

    def load(self) -> SeedsResult:
        """ Загружает результаты сидинга из файла.
            :return: Объект SeedsResult, содержащий данные, загруженные из файла. """
        logger.info(f"[{self.scenario}] Загружает результаты сидинга из файла")
        result = load_seeds_result(scenario=self.scenario)
        logger.info(f"[{self.scenario}] Результат сидинга загружен из файла успешно")
        return result

    def build(self) -> None:
        """ Генерирует данные с помощью билдера, используя план сидинга, и сохраняет результат. """
        plan_json = self.plan.model_dump_json(indent=2, exclude_defaults=True)
        logger.info(f"[{self.scenario}] Старт генерации сидинга для плана: {plan_json}")
        result = self.builder.build(self.plan)
        logger.info(f"[{self.scenario}] Генерации данных сидинга выполнена")
        self.save(result)
