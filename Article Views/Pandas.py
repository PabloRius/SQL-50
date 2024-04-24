import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({'id': sorted(views[(views['viewer_id'] == views['author_id'])]['viewer_id'].unique())})