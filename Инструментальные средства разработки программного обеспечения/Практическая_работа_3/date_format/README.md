# date_format

Практическая работа №3: сравнение форматов JSON, XML, YAML, MessagePack, CBOR и Protobuf.

Установка: `pip install -r requirements.txt`
Запуск: `python run_all.py` (сводная таблица), `python server.py` и `python client.py <json|msgpack|cbor|protobuf>` (передача по TCP).
Схема Protobuf: `profile.proto`, компиляция `protoc --python_out=. profile.proto`.
