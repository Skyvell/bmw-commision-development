from io import BytesIO
import pandas as pd


class VolumeTargetsParser:
    def parse_volume_targets(self, file_content):
        df = pd.read_excel(BytesIO(file_content))
        df = df.dropna(how='all').dropna(how='all', axis=1)
        columns = df.columns.to_list()
        items = [
            {
                'agent': row[columns[0]],
                'year_month': month,
                'target': int(row[month])
            }
            for index, row in df.iterrows()
            for month in columns[1:]
        ]
        return items