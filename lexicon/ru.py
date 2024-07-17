from dataclasses import dataclass


@dataclass
class Lexicon:
    helptext: str = \
        "📱Для того чтобы отправить заявку, выберите категорию и следуйте "\
        "указаниям бота.\n"\
        "Оставить заявку - /submit_application"
    back: str = "Вернуться"
    submit_application: str = "Оставить заявку"
    select_a_category: str = "Выберите категорию:"
    select_a_service: str = "Выберите проблему:"
    input_street: str = "Введите название улицы"
    input_house: str = "Введите номер дома"
    input_flat: str = "Введите номер квартиры"
    input_name: str = "Введите ФИО"
    input_phone: str = "Введите номер телефона"
    input_text: str = "Опишите суть вашей проблемы"
    input_personal_account: str = "Введите номер лицевого счёта"
    category: str = "Категория"
    service: str = "Проблема"
    street: str = "Улица"
    house: str = "Дом"
    flat: str = "Квартира"
    name: str = "ФИО"
    phone: str = "Телефон"
    text: str = "Описание"
    personal_account: str = "Лицевой счёт"
    sent_application: str = "Отправить заявку"
    not_found_input_street: str = \
        "Улица с таким названием отсутствует в информационной системе"
    not_found_input_house: str = \
        "Дом с таким номером отсутствует в информационной системе"
    not_found_input_flat: str = \
        "Квартира с таким номером отсутствует в информационной системе"
    error_input_name: str = "Длина ФИО превышает ограничение системы"
    error_input_phone: str = "Вы ввели некорректный номер телефона"
    error_input_text: str = "Длина текста превышает ограничение системы"
    error_input_personal_account: str = "Вы ввели некорректный лицевой счёт"
    error_personal_account: str = "Лицевой счёт не привязан к данному адресу"
    accepted: str = "Заявка принята."
    application_number: str = "Номер заявки"
    control_name: str = "Наименование Управляющей компании"

    categories: str = "Категории"
    services: str = "Проблемы"



    cancel: str = "Действие отменено"
    api_not_available = "Сервис временно не доступен"
    send_contact = "📱 Отправить"
    enter_phone = "📱 Ввести вручную"
    click_button = "Нажмите на кнопку ниже, чтобы отправить контакт"


@dataclass
class Commands:
    help: str = "Помощь"
    submit_application: str = "Оставить заявку"
    cancel: str = "Отменить действие"
