install:
	poetry install # эта команда полезна при первом клонировании репозитория (или после удаления зависимостей)

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run # публикация (обновление) пакетов в каталоге PyPI. Для отладки публикации мы будем использовать аргумент --dry-run, чтобы не добавлять пакет в каталог PyPI

package-install:
	python3 -m pip install --user dist/*.whl # Для установки пакета из операционной системы. Её необходимо запускать из корневой директории проекта.

lint:
	poetry run flake8 brain_games

brain-even:
	poetry run brain-even