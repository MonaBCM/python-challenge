{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7cf20e7e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import os\n",
    "import csv\n",
    "\n",
    "csvpath=os.path.join('Resources','budget_data.csv')\n",
    "budget_data_df= pd.read_csv(csvpath, encoding=\"utf-8\")\n",
    "print(budget_data_df.head())\n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fe275b82",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Total change in the period is calculated by sum function\n",
    "Total_PL=sum(budget_data_df[\"Profit/Losses\"])\n",
    "print(Total_PL) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4dc16269",
   "metadata": {},
   "outputs": [],
   "source": [
    "# month count is done through len function which return the unique values\n",
    "month_count=len(budget_data_df[\"Date\"].unique())\n",
    "print(month_count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3d3232f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# df.diff function is used to find differences in the profit\\Losses column by indexing by date\n",
    "df=budget_data_df.set_index('Date')\n",
    "result=df.diff()\n",
    "result\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "97793c71",
   "metadata": {},
   "outputs": [],
   "source": [
    "Average_change=result.mean()\n",
    "print(Average_change)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3134b18b",
   "metadata": {},
   "outputs": [],
   "source": [
    "Greatest_increase= df.diff(periods=-1).max()\n",
    "print(Greatest_increase)\n",
    "Greatest_decrease=df.diff(periods=-1).min()\n",
    "print(Greatest_decrease)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "39a84f97",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"----------------------------------------------------------\")\n",
    "print(\"Financial Analysis\")\n",
    "print(\"----------------------------------------------------------\")\n",
    "print(\"Total Months: \" + str(month_count))\n",
    "print(\"Total Profits: \" + \"$\" + str(Total_PL))\n",
    "print(\"Average Change: \" + \"$\" + str(int(Average_change)))\n",
    "print(\"Greatest Increase in Profits: \" +  \" ($\" + str(int(Greatest_increase))+\")\")\n",
    "print(\"Greatest Increase in Profits: \" +  \" ($\" + str(int(Greatest_decrease))+\")\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "322e721d",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('financial_analysis.txt', 'w') as text:\n",
    "    text.write(\"----------------------------------------------------------\\n\")\n",
    "    text.write(\"  Financial Analysis\"+ \"\\n\")\n",
    "    text.write(\"----------------------------------------------------------\\n\\n\")\n",
    "    text.write(\"    Total Months: \" + str(month_count) + \"\\n\")\n",
    "    text.write(\"    Total Profits: \" + \"$\" + str(Total_PL) +\"\\n\")\n",
    "    text.write(\"    Average Change: \" + '$' + str(int(Average_change)) + \"\\n\")\n",
    "    text.write(\"Greatest Increase in Profits: \" +  \" ($\" + str(int(Greatest_increase))+\")\\n\")\n",
    "    text.write(\"Greatest Increase in Profits: \" +  \" ($\" + str(int(Greatest_decrease))+\")\\n\")\n",
    "    text.write(\"----------------------------------------------------------\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a1e19921",
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
