from app.database.models import async_session
from app.database.models import User, Category, Item, Basket
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


async def set_item(it_name, it_decr, it_price, it_category):
    async with async_session() as session:
        name = await session.scalar(select(Item).where(Item.name == it_name))
        descr = await session.scalar(select(Item).where(Item.description == it_decr))
        price = await session.scalar(select(Item).where(Item.price == it_price))
        category = await session.scalar(select(Item).where(Item.category == it_category))
        if not name:
            session.add(
                Item(name=it_name, description=it_decr, price=it_price, category=it_category))
            await session.commit()


async def get_categories():
    async with async_session() as session:
        return await session.scalars(select(Category))


async def item_category_item(category_id):
    async with async_session() as session:
        return await session.scalars(select(Item).where(Item.category == category_id))


async def get_item(item_id):
    async with async_session() as session:
        return await session.scalar(select(Item).where(Item.id == item_id))


async def add_basket(user_id, item_name):
    async with async_session() as session:
        session.add(Basket(user=user_id, item=item_name))
        await session.commit()


async def get_basket(user_id):
    async with async_session() as session:
        return await session.scalars(select(Basket).where(Basket.user == user_id))
