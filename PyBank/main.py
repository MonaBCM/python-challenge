{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "07615786",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "375aa3b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Resources\\budget_data.csv\n",
      "     Date  Profit/Losses\n",
      "0  Jan-10        1088983\n",
      "1  Feb-10        -354534\n",
      "2  Mar-10         276622\n",
      "3  Apr-10        -728133\n",
      "4  May-10         852993\n"
     ]
    }
   ],
   "source": [
    "# import Dependencies\n",
    "\n",
    "import pandas as pd\n",
    "import os\n",
    "import csv\n",
    "\n",
    "csvpath=os.path.join('Resources','budget_data.csv')\n",
    "print(csvpath)\n",
    "\n",
    "budget_data_df= pd.read_csv(csvpath, encoding=\"utf-8\")\n",
    "print(budget_data_df.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8f5d8761",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "86\n"
     ]
    }
   ],
   "source": [
    "Month_count=0\n",
    "month_count=len(budget_data_df[\"Date\"].unique()) \n",
    "print(month_count) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "2facdf2d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "22564198\n"
     ]
    }
   ],
   "source": [
    "Total_PL=sum(budget_data_df[\"Profit/Losses\"])\n",
    "print(Total_PL)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "82a35e14",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Profit/Losses</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>-1443517.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>631156.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>-1004755.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1581126.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>81</th>\n",
       "      <td>-1627245.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>82</th>\n",
       "      <td>616795.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>83</th>\n",
       "      <td>628522.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>84</th>\n",
       "      <td>90895.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>85</th>\n",
       "      <td>-224669.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>86 rows × 1 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    Profit/Losses\n",
       "0             NaN\n",
       "1      -1443517.0\n",
       "2        631156.0\n",
       "3      -1004755.0\n",
       "4       1581126.0\n",
       "..            ...\n",
       "81     -1627245.0\n",
       "82       616795.0\n",
       "83       628522.0\n",
       "84        90895.0\n",
       "85      -224669.0\n",
       "\n",
       "[86 rows x 1 columns]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame(budget_data_df[\"Profit/Losses\"])\n",
    "df.diff()\n",
    " \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "97efed24",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Profit/Losses    8311.105882\n",
      "dtype: float64\n",
      "Profit/Losses    1825558.0\n",
      "dtype: float64\n",
      "Profit/Losses   -1862002.0\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "Average_Change=df.diff(periods=-1).mean()\n",
    "print(Average_Change)\n",
    "Greatest_increase= df.diff(periods=-1).max()\n",
    "print(Greatest_increase)\n",
    "Greatest_decrease=df.diff(periods=-1).min()\n",
    "print(Greatest_decrease)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "872464d5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "----------------------------------------------------------\n",
      "Financial Analysis\n",
      "----------------------------------------------------------\n",
      "Total Months: 86\n",
      "Total Profits: $22564198\n",
      "Average Change: $8311\n",
      "Greatest Increase in Profits:  ($1825558)\n",
      "Greatest Decrease in Profits:  ($-1862002)\n",
      "----------------------------------------------------------\n"
     ]
    }
   ],
   "source": [
    "print(\"----------------------------------------------------------\")\n",
    "print(\"Financial Analysis\")\n",
    "print(\"----------------------------------------------------------\")\n",
    "print(\"Total Months: \" + str(month_count))\n",
    "print(\"Total Profits: \" + \"$\" + str(Total_PL))\n",
    "print(\"Average Change: \" + \"$\" + str(int(Average_Change)))\n",
    "print(\"Greatest Increase in Profits: \"  + \" ($\" + str(int(Greatest_increase))+\")\")\n",
    "print(\"Greatest Decrease in Profits: \"  + \" ($\" + str(int(Greatest_decrease))+\")\")\n",
    "print(\"----------------------------------------------------------\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "2d607b05",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('financial_analysis.txt', 'w') as text:\n",
    "    text.write(\"----------------------------------------------------------\\n\")\n",
    "    text.write(\"  Financial Analysis\"+ \"\\n\")\n",
    "    text.write(\"----------------------------------------------------------\\n\\n\")\n",
    "    text.write(\"    Total Months: \" + str(month_count) + \"\\n\")\n",
    "    text.write(\"    Total Profits: \" + \"$\" + str(Total_PL) +\"\\n\")\n",
    "    text.write(\"    Average Change: \" + '$' + str(int(Average_Change)) + \"\\n\")\n",
    "    text.write(\"    Greatest Increase in Profits: \" +  \" ($\" + str(int(Greatest_increase))+\")\\n\")\n",
    "    text.write(\"    Greatest Decrease in Profits: \" +  \" ($\" +  str(int(Greatest_decrease))+\")\\n\")\n",
    "    text.write(\"----------------------------------------------------------\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab50998f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
