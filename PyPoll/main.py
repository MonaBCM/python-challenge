{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "252ddb4a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Resources\\election_data.csv\n",
      "   Ballot ID     County                Candidate\n",
      "0    1323913  Jefferson  Charles Casper Stockham\n",
      "1    1005842  Jefferson  Charles Casper Stockham\n",
      "2    1880345  Jefferson  Charles Casper Stockham\n",
      "3    1600337  Jefferson  Charles Casper Stockham\n",
      "4    1835994  Jefferson  Charles Casper Stockham\n"
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
    "csvpath=os.path.join('Resources','election_data.csv')\n",
    "print(csvpath)\n",
    "\n",
    "election_df= pd.read_csv(csvpath, encoding=\"utf-8\")\n",
    "print(election_df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3c7bdd7b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "369711\n"
     ]
    }
   ],
   "source": [
    "Total_votes=len(election_df[\"Ballot ID\"].unique()) \n",
    "print(Total_votes)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6eb1190b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                         Ballot ID  County\n",
      "Candidate                                 \n",
      "Charles Casper Stockham      85213   85213\n",
      "Diana DeGette               272892  272892\n",
      "Raymon Anthony Doane         11606   11606\n"
     ]
    }
   ],
   "source": [
    "results=election_df.groupby(['Candidate'],as_index=1).count()\n",
    "print(results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1b9d2c5e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ballot ID    272892\n",
      "County       272892\n",
      "dtype: int64\n",
      "Ballot ID    11606\n",
      "County       11606\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "Winner=results.max()\n",
    "print(Winner)\n",
    "thirdrun=results.min()\n",
    "print(thirdrun)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b7353067",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ballot ID    0.738122\n",
      "County       0.738122\n",
      "dtype: float64\n",
      "Ballot ID    0.031392\n",
      "County       0.031392\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "WinnerP=(Winner/Total_votes)\n",
    "print(WinnerP)\n",
    "ThirdrunP=(thirdrun/Total_votes)\n",
    "print(ThirdrunP)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7456af3b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "----------------------------------------------------------\n",
      "Election Results\n",
      "----------------------------------------------------------\n",
      "Total Votes: 369711\n",
      "----------------------------------------------------------\n"
     ]
    }
   ],
   "source": [
    "print(\"----------------------------------------------------------\")\n",
    "print(\"Election Results\")\n",
    "print(\"----------------------------------------------------------\")\n",
    "print(\"Total Votes: \" + str(Total_votes))\n",
    "print(\"----------------------------------------------------------\")\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "65095a58",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('election results.txt', 'w') as text:\n",
    "    text.write(\"----------------------------------------------------------\\n\")\n",
    "    text.write(\"  Election Results\"+ \"\\n\")\n",
    "    text.write(\"----------------------------------------------------------\\n\\n\")\n",
    "    text.write(\"  Total Votes: \" + str(Total_votes) + \"\\n\")\n",
    "    \n",
    "    text.write(\"----------------------------------------------------------\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7675e9da",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e02102b1",
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
