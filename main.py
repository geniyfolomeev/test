# Пример теста
@pytest.mark.API
def test_get_spec_calendar_by_id(special_calendar_fixture):
    """Получение календаря по его id"""
    response = SpecialCalendarApi.get_special_calendar_by_id(special_calendar_fixture.calendar.id)
    assert response.status_code == 200
    assert_schema(instance=response.json(), model=SpecCalendarResponse)
    response_body: SpecCalendarResponse = SpecCalendarResponse.parse_obj(response.json())
    assert_response(actual_response=response_body.calendar, expected_response=special_calendar_fixture.calendar)


# Фикстура
@pytest.fixture(autouse=False, scope="function")
def special_calendar_fixture() -> SpecCalendarResponse:
    """Create special calendar before test and delete it after test execution"""
    calendar = SpecCalendarRequest()
    response = SpecialCalendarApi.create_spec_calendar(calendar)
    assert response.status_code == 200
    response_body: SpecCalendarResponse = SpecCalendarResponse.parse_obj(response.json())
    yield response_body
    SpecialCalendarApi.delete_special_calendar_db(response_body.calendar.id)


# Проверка схемы ответа
@allure.step("Проверяем схему ответа")
def assert_schema(instance: dict, model: Type[BaseModel]):
    """Assertion for response schema. Trying to parse instance to model, described as a class.

    :param instance: response dictionary
    :param model: response model"""
    logger.info("Проверяем схему ответа")
    try:
        model.parse_obj(instance)
    except ValidationError as e:
        logger.error(f"Невалидная схема ответа:\n{e}")
        raise AssertionError(e)


# Проверка тела ответа
@allure.step("Проверяем ответ")
def assert_response(actual_response, expected_response, exclude_keys: list = None):
    """Assertion for HTTP response.

    Use case: actual response contains a lot of expected response attributes, so
    instead of asserting them one by one, you can call this function.

    :param actual_response: instance of response model, contains expected response fields
    :param expected_response: instance of expected response model
    :param exclude_keys: list of attributes which should be checked during the comparison"""
    logger.info("Проверяем ответ")
    for attribute in expected_response.dict().keys():
        if exclude_keys is not None and attribute in exclude_keys:
            continue
        with allure.step(f"Сверяем значения атрибута {attribute}"):
            logger.info(f"Сверяем значения атрибута {attribute}")
            try:
                actual_value = getattr(actual_response, attribute)
                expected_value = getattr(expected_response, attribute)
                assert actual_value == expected_value, f'\nExpected: {expected_value}\nGot: {actual_value}'
            except AttributeError as e:
                logger.error(f"В полученном ответе нет атрибута {attribute}")
                raise AssertionError(e)


# Кусок апи клиента
class SpecialCalendarApi:
    """ссыль на сваггер"""

    @classmethod
    @allure.step("Создаем специальный календарь по API")
    def create_spec_calendar(cls, body: SpecCalendarRequest) -> Response:
        return post_request(url='/special-calendar/v1/calendars/', body=body.dict(by_alias=True))

    ...


# Модель запроса
class SpecCalendarRequest(BaseModel):
    date_end: StrictStr = Field(default="9999-12-31", alias="dateEnd")
    name: StrictStr = Field(default_factory=generate_string)
