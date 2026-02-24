# Zomato Data Analysis
'''
Understanding Customer Preferences And Restaurant Trends For Making
Informed Business Decisions In Food Industry.
'''
#Importing Necessary Libraries
import numpy as np,pandas as pd
import matplotlib.pyplot as plt,seaborn as sns
import os

class Food_Service:
    
    def __init__(self,filepath="Zomato-data-.csv"):
        self.fpath=filepath
        self.df=None
        self.load_data()
    
    def load_data(self):
        #Loading Dataset From CSV
        try:
            self.df=pd.read_csv(self.fpath)
            self.cleaning()
            print(f"\nData Loaded Successfully.\nTotal records:{len(self.df)}")
        except FileNotFoundError:
            print(f"Error: File {self.filepath} Not Found.")
            self.df=pd.DataFrame()
    
    def cleaning(self):
        #Data Cleaning And Preparation
        if self.df is not None and not self.df.empty:
            '''
            Converting The Rate Column To A Float By 
            Removing Denominator Characters
            '''
            def ratehandler(val):
                val=str(val).split('/')
                val=val[0]
                return float(val)
            
            if 'rate' in self.df.columns:
                self.df['rate']=self.df['rate'].apply(ratehandler)
    
    def create_restaurant(self,restaurant_data):
        #Adding A New Restaurant Record"""
        try:
            new_r=pd.DataFrame([restaurant_data])
            self.df=pd.concat([self.df,new_r],ignore_index=True)
            self.save_data()
            print(f"Restaurant '{restaurant_data.get('name','Unknown')}' Added Successfully!")
            return True
        except Exception as e:
            print(f"Error Creating Restaurant: {e}")
            return False
        
    def read_all_restaurants(self):
        #Displaying All Restaurant Records
        if self.df is None or self.df.empty:
            print("No Data Available")
            return
        print("\n")
        print("All Restaurants")
        print(self.df.to_string())
    
    def read_by_name(self,name):
        #Getting Restaurant By Name
        if self.df is None or self.df.empty:
            print("No Data Available")
            return None
        res=self.df[self.df['name'].str.contains(name,case=False,na=False)]
        if res.empty:
            print(f"No Restaurant Found With Name Containing '{name}'")
            return None
        print("\n")
        print(res.to_string())
        return res
    
    def read_info(self):
        #Getting Summary Of The Dataframe
        if self.df is None or self.df.empty:
            print("No Data Available")
            return
        print("\nDataFrame Info:")
        print(self.df.info())
        print("\nNull Values:")
        print(self.df.isnull().sum())
    
    def update_restaurant(self,index,updates):
        #Updating An Existing Restaurant Record
        try:
            if index<0 or index>=len(self.df):
                print(f"Invalid Index: {index}")
                return False
            for i,j in updates.items():
                if i in self.df.columns:
                    self.df.at[index,i]=j
            self.save_data()
            print(f"Restaurant At Index {index} Updated Successfully")
            return True
        except Exception as e:
            print(f"Error Updating Restaurant: {e}")
            return False
    
    def delete_restaurant(self,index):
        #Removing A Restaurant Record
        try:
            if index<0 or index>=len(self.df):
                print(f"Invalid Index: {index}")
                return False
            name=self.df.at[index,'name']
            self.df=self.df.drop(index).reset_index(drop=True)
            self.save_data()
            print(f"Restaurant '{name}' Deleted Successfully!")
            return True
        except Exception as e:
            print(f"Error Deleting Restaurant: {e}")
            return False
    
    def save_data(self):
        #Saving Data To CSV File
        try:
            self.df.to_csv(self.fpath,index=False)
            print(f"Data Saved To {self.filepath}")
        except Exception as e:
            print(f"Error Saving Data: {e}")
    
    #Analysis Functions
    
    def explore_types(self):
        #Exploring Restaurant Types
        if self.df is None or self.df.empty:
            print("No Data Available.")
            return
        
        plt.figure(figsize=(10,5))
        sns.countplot(x=self.df['listed_in(type)'])
        plt.xlabel('Type Of Restaurant')
        plt.ylabel('Count')
        plt.title('Restaurant Types Distribution')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    def votes_by_type(self):
        #Analyzing Votes By Restaurant Type
        if self.df is None or self.df.empty:
            print("No Data Available.")
            return
        
        groupdata=self.df.groupby('listed_in(type)')['votes'].sum()
        res=pd.DataFrame({'votes': groupdata})
        plt.figure(figsize=(10,5))
        plt.plot(res,c='green',marker='o',linewidth=2)
        plt.xlabel('Type Of Restaurant')
        plt.ylabel('Votes')
        plt.title('Total Votes by Restaurant Type')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    def most_voted(self):
        #Identifying The Most Voted Restaurant
        if self.df is None or self.df.empty:
            print("No Data Available")
            return
        maxvotes=self.df['votes'].max()
        max_votedrestaur=self.df.loc[self.df['votes']==maxvotes,'name']
        print('\n')
        print('Restaurant(s) With Maximum Votes:')
        for i in max_votedrestaur:
            print(f"-> {i} ({maxvotes} Votes)")
    
    def online_availability(self):
        #Online Order Availability Analysis
        if self.df is None or self.df.empty:
            print("No Data Available.")
            return
        plt.figure(figsize=(8,5))
        sns.countplot(x=self.df['online_order'])
        plt.xlabel('Online Order Availability')
        plt.ylabel('Count')
        plt.title('Online Order Availability')
        plt.tight_layout()
        plt.show()
    
    def analyze_ratings(self):
        #Analyzing Ratings Distribution
        if self.df is None or self.df.empty:
            print("No Data Available.")
            return
        plt.figure(figsize=(10,5))
        plt.hist(self.df['rate'],bins=5,color='skyblue',edgecolor='black')
        plt.title('Rating Distribution')
        plt.xlabel('Rating')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()
    
    def approx_cost(self):
        #Approximate Cost For Family Analysis
        if self.df is None or self.df.empty:
            print("No Data Available.")
            return
        plt.figure(figsize=(12,5))
        sns.countplot(x=self.df['approx_cost(for two people)'])
        plt.xlabel('Approximate Cost (For Two People)')
        plt.ylabel('Count')
        plt.title('Approximate Cost Distribution')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    def rate_online_vs_offline(self):
        #Ratings Comparison-->Online vs Offline"""
        if self.df is None or self.df.empty:
            print("No Data Available")
            return
        plt.figure(figsize=(8,6))
        sns.boxplot(x='online_order',y='rate',data=self.df)
        plt.xlabel('Online Order Availability')
        plt.ylabel('Rating')
        plt.title('Ratings Comparison: Online vs Offline')
        plt.tight_layout()
        plt.show()
    
    def order_mode_by_type(self):
        #Order Mode Preference By Restaurant Type
        if self.df is None or self.df.empty:
            print("No Data Available")
            return
        pt=self.df.pivot_table(index='listed_in(type)',columns='online_order',
                                aggfunc='size',fill_value=0)
        plt.figure(figsize=(10,6))
        sns.heatmap(pt,annot=True,cmap='YlGnBu',fmt='d',cbar_kws={'label':'Count'})
        plt.title('Order Mode by Restaurant Type::Heatmap')
        plt.xlabel('Online Order Availability')
        plt.ylabel('Restaurant Type')
        plt.tight_layout()
        plt.show()
    
    def display_menu(self):
        #Displaying Menu
        while True:
            print("Zomato Data Analysis")
            print("\n---Operations---")
            print("1.Create::Add New Restaurant")
            print("2.Read::View All Restaurants")
            print("3.Read::Search Restaurant By Name")
            print("4.Read::View Data Info & Null Values")
            print("5.Update::Modify Restaurant Data")
            print("6.Delete::Remove Restaurant")

            print("\n---Analysis And Visualization---")
            print("Explore Restaurant Types::")
            print("Analyze Votes By Type")
            print("Find Most Voted Restaurant")
            print("Analyze Online Order Availability")
            print("Analyze Ratings Distribution")
            print("Analyze Approximate Cost")
            print("Compare Ratings (Online vs Offline)")
            print("Order Mode By Restaurant Type (Heatmap)")

            print("\nSave & Exit")

            ch=input("Enter Your Choice (1-15): ").strip()
            match ch:
                case '1':
                    self.create()
                case '2':
                    self.read_all_restaurants()
                case '3':
                    name=input("Enter Restaurant Name To Search: ")
                    self.read_by_name(name)
                case '4':
                    self.read_info()
                case '5':
                    self.update()
                case '6':
                    self.delete()
                case '7':
                    self.explore_types()
                case '8':
                    self.votes_by_type()
                case '9':
                    self.most_voted()
                case '10':
                    self.online_availability()
                case '11':
                    self.analyze_ratings()
                case '12':
                    self.approx_cost()
                case '13':
                    self.rate_online_vs_offline()
                case '14':
                    self.order_mode_by_type()
                case '15':
                    self.save_data()
                    break
                case _:
                    print("Invalid Choice")

    def create(self):
        #Menu For Creating A New Restaurant
        print("\n---Add New Restaurant---")
        try:
            data={}
            col=self.df.columns.tolist() if self.df is not None else []
            for i in col:
                val=input(f"Enter {i}:").strip()
                if i=='rate':
                    data[i]=float(val) if val else 0.0
                elif i=='votes':
                    data[i]=int(val) if val else 0
                else:
                    data[i]=val
            self.create_restaurant(data)
        except ValueError:
            print("Invalid Input")
    
    def update(self):
        #Menu For Updating A Restaurant
        print("\n---Update Restaurant---")
        try:
            index=int(input("Enter Restaurant Index To Update: "))
            print("\nCurrent Data:")
            print(self.df.iloc[index])
            col=input("\nEnter Column Name To Update: ").strip()
            val=input(f"Enter New Value For {col}: ").strip()
            # Type Conversion Based On Column
            if col=='rate':
                val=float(val)
            elif col=='votes':
                val=int(val)
            self.update_restaurant(index,{col: val})
        except(ValueError,IndexError):
            print("Invalid Input")
    
    def delete(self):
        #Menu For Deleting A Restaurant"""
        print("\n---Delete Restaurant---")
        try:
            index=int(input("Enter Restaurant Index To Delete: "))
            conf=input(f"Are You Sure You Want To Delete Restaurant At Index {index}? (Y/N): ")
            if conf.lower()=='Y':
                self.delete_restaurant(index)
        except ValueError:
            print("Invalid Input")


#Main
if __name__=="__main__":
    zomato = Food_Service("Zomato-data-.csv")
    zomato.display_menu()