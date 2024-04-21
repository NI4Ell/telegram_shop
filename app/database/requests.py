from app.database.models import async_session
from app.database.models import User, Category, Item
from sqlalchemy import select


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def set_category(cat_name):
    async with async_session() as session:
        category = await session.scalar(select(Category).where(Category.name == cat_name))

        if not category:
            session.add(Category(name=cat_name))
            await session.commit()


async def set_item(it_name, it_decr, it_price):
    async with async_session() as session:
        name = await session.scalar(select(Item).where(Item.name == it_name))
        descr = await session.scalar(select(Item).where(Item.description == it_decr))
        price = await session.scalar(select(Item).where(Item.price == it_price))
        if not name:
            session.add(
                Item(name=it_name, description=it_decr, price=it_price))
            await session.commit()
