from ..connect import users_collection as user_coll

from utils.logging import logger


async def get_user(user_id: int) -> dict | None:
    """Возвращает пользователя по его id"""
    try:
        user = await user_coll.find_one({"id": user_id})
        return user
    except Exception as e:
        logger.error(f"Error getting user {user_id}: {e}")
        return None


async def get_or_create_user(user_id: int, username: str = None, language: str = None) -> dict:
    """Возвращает пользователя по его id, если его нет - создает"""
    if user := await get_user(user_id):
        return user

    return await create_user(user_id, username, language)


async def create_user(user_id: int, username: str = None, language: str = None) -> dict:
    """Создает нового пользователя"""
    user_data = {
        "id": user_id,
        "username": username,
        "language": language,
        "referral": 0,
        "is_banned": False,
    }
    logger.info(f"New user: {user_id} | {username}")
    await user_coll.insert_one(user_data)
    return user_data


async def update_user_username(user_id: int, username: str = None) -> None:
    """Обновляет данные пользователя"""
    result = await user_coll.update_one({"id": user_id}, {"$set": {"username": username}})
    if result.modified_count > 0:
        logger.info(f"Update user: {user_id} | {username}")


async def new_referral(inviter_id: int) -> None:
    """Добавляет приведенного реферала к пользователю inviter_id"""
    result = await user_coll.update_one({"id": inviter_id}, {"$inc": {"referral": 1}})
    if result.modified_count > 0:
        logger.info(f"User: {inviter_id} | привел нового пользователя")


async def change_language(user_id: int, language: str) -> None:
    """Изменяет язык пользователя на language"""
    result = await user_coll.update_one({"id": user_id}, {"$set": {"language": language}})
    if result.modified_count > 0:
        logger.info(f"User: {user_id} | изменил язык на - {language}")


async def ban_or_unban_user(user_id: int, is_banned: bool) -> None:
    """Меняет статус блокировки пользователя на заданный"""
    result = await user_coll.update_one({"id": user_id}, {"$set": {"is_banned": is_banned}})
    if result.modified_count > 0:
        logger.info(f"User: {user_id} | статус блокировки изменен на - {is_banned}")
