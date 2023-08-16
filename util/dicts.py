
categories = {
    'Auto': ['Gas','Maintenance', 'Upgrades', 'Other_Auto'],
    'Baby': ['Diapers', 'Formula', 'Clothes', 'Toys', 'Other_Baby'],
    'Clothes': ['Clothes', 'Shoes', 'Jewelry', 'Sunglasses', 'Bags_Accessories'],
    'Entertainment': ['Sports_Outdoors', 'Theater', 'DateNights', 'Arts_Crafts', 'Books', 'Games', 'Guns', 'E_Other'],
    'Electronics': ['Accessories', 'Computer', 'TV', 'Camera', 'Phone','Tablet_Watch', 'Gaming', 'Electronics_misc'],
    'Food': ['Groceries', 'FastFood_Restaurants'],
    'Home': ['Maintenance', 'Furniture_Appliances', 'Hygiene', 'Gym',
        'Home_Essentials', 'Kitchen', 'Decor', 'Security', 'Yard_Garden', 'Tools'],
    'Medical': ['Bills', 'Health_Wellness'],
    'Kids': ['K_Toys'],
    'Personal_Care': ['Hair', 'Makeup_Nails', 'Beauty', 'Massage','Vitamins_Supplements', 'PC_Other'],
    'Pets': ['Pet_Food', 'Pet_Toys', 'Pet_Med', 'Pet_Other'],
    'Subscriptions_Memberships': ['Entertainment', 'Gym', 'Sub_Other'],
    'Travel': ['Hotels', 'Flights', 'Car_Rental', 'Activities']}



amz_categories = {
    'Auto': ['Automotive |'],
    'Bdays Holidays': [],
    'Charity': [],
    'Clothes': ['Clothing, Shoes & Jewelry |',],
    'Entertainment': ['Arts, Crafts & Sewing |',],
    'Electronics': ['Computer', 'TV', 'PC', 'Sound', 'Camera', 'Phone', 'Gaming', 'Other'],
    'Food': ['Grocery & Gourmet Food |'],
    'Home': ['Health & Household | Household Supplies |', 'Home & Kitchen | Bedding |'],
    'Medical': [],
    'Kids': ['Baby Products |'],
    'Personal_Care': ['Beauty & Personal Care |'],
    'Pets': ['Pet_Food', 'Pet Toys', 'Pet Grooming', 'Pet Med', 'Pet Other'],
    'Subscriptions_Memberships': ['Entertainment', 'Gym', 'Sub_Other'],
    'Utilities': ['Electricity', 'Water', 'Internet', 'Phone', 'Gas', 'Trash'],
    'Vacation': ['Hotels', 'Flights', 'Rental Cars', 'Activities', 'Souvenirs' 'Other'],
    'Savings': ['Savings', 'College Fund', 'Investments', 'Emergency', 'Retirement', 'Other']

}

walmart_sub_dict = {
    'Other-Auto': ['Off-Road', 'Auto Interior', 'Auto Electronics', 'Automotive Interior', 'Auto Detailing', 'Auto & Tires'],
    'Maintenance/Fees': ['Auto & Tires|Automotive Replacement Parts', 'Automotive Tools & Equipment', 'Oils and FLuids', 'Motorcycle', 'Oil and Fluids', 'Tires'],
    'Baby': ['Baby|B', 'Baby|C', 'Baby|Diapering', 'Baby|N', 'Baby|Feeding', 'Baby|Strollers', 'Baby Bath', 'Baby Gates', 'Baby Health Care',
            'Baby Monitors', 'Baby Proofing', 'Babyproofing', 'Child Proof', 'Playards','Toddlers Room', 'Toddler'],
    'Misc/Entertainment': ['Sewing', 'Musical Instruments'],
    'Electronics': ['Cellphones|', 'Electronics', 'Cell Phones'],
    'Movies/TV/Music': ['Movies & TV', 'Music|'],
    'Clothes/Jewelry': ["Clothing|", 'Jewelry|' ],
    'Groceries': ['Food|', 'Keto Diet', 'Fitness|Protein Bars', 'Fitness | Protein Shakes', 'Superfoods & Cleanses', 'Diet Shakes', 'MCT Oil', 'Meal Replacements',
                'Ensure |', 'On-the-Go Nutrition',],
    'Health-Related': ['First Aid', 'Ear Care|', 'Eye Care|', 'Foot Care', 'Gas Relief', 'Home Health Care', 'Laxatives', 'Lip Care',
                'Medicine Cabinet', 'Pain Relievers','Health Essentials'],
    'Furniture/Appliances': ['Home|Furniture','Furniture'],
    'Electronics': ['Computers', 'Projection Equipment', 'Health|'],
    'Office': ['Office Supplies', 'Office'],
    'Decor': [ 'Home|Decor', 'Home|Bedding', 'Home|Bath', 'Home|Appliances', 'Kids Rooms', 'Kitchen & Dining', 'Teens Rooms'],
    'Home Essentials': ['Cleaning Supplies', 'Household Essentials', 
                'Party & Occasions', 'Bath & Body', 'Deodorants & Antiperspirants', 
                'Feminine Care', 'Mens Essentials', 'Oral Care', 'Shaving', 
                'Sun Care', 'Hand Soaps', 'Bath Bombs, Bubble Baths', 'College Hair Essentials', 'Fragrances',
                'ChapStick', 'Beauty by Topic', 'Beauty Next Day', 'Beauty Stock Up', 'Beauty Wellness', 'Cologne for Men',
                'All Fragrances', 'Perfume for Women', 'Hair Care', 'Here for Every Beauty', 'Beauty|Makeup', 'Premium Beauty',
                'Beauty|Shop by Concern', 'Skin Care', 'Equate|', 'Family Planning', 'Fiber Supplements', 
                'Sexual Wellness', 'Sleep & Snoring', 'Sports Medicine',
                'Storage & Organization', 'Personal Care'],
    'Maintenance-Home': ['Home Improvement', 'Patio & Garden'],
    'Tools': ['Industrial'],
    'Pets': ['Pets'],
    'Sports/Outdoors': ['Sports & Outdoors'],
    'Other': ['Games & Puzzles', 'Books|', 'Video Games'],
    'Toys': ['Hobby &','Arts & Crafts for Kids','Remote Control & Play Vehicles','Outdoor Play','Kids Bikes & Riding', 'Toys by Age', 'Stuffed Animals', 'Toys by Price', ],
    'Vitamins/Supplements': ['Vitamins & Supplements', 'Probiotics|', 'Fitness|Amino', 'Fitness|Ancient', 'Fitness|Arginine', 'Fitness|BCAA', 'Fitness|Creatine', 'Fitness|Energy', 'Fitness|Fuel', 'Fitness|Glutamine', 'Fitness|GNC', 'Fitness|L-Carnitine',
                'Fitness|Lysine', 'Fitness|Muscle',
                'Fitness|Organic', 'Fitness|Optimum', 'Fitness|Performance', 'Fitness|Pre', 'Fitness|Protein Powder',
                'Fitness|Vegan', 'Fitness|Winter', 'Fat Blockers', 'Fat Burners', 'Weight Loss Pills']}





'''if __name__ == "__main__":
    merged_df = merge_csv_files("C:\\Users\\Jordan Convey\\Documents\\GitHub\\Finance\\Categorize Bank Descriptions\\Training Data\\BigBasketProducts Dataset.csv", 
        "C:\\Users\\Jordan Convey\\Documents\\GitHub\Finance\\Categorize Bank Descriptions\\Training Data\\AMZ Electronics Dataset.csv", 
        "C:\\Users\\Jordan Convey\\Documents\\GitHub\\Finance\\Categorize Bank Descriptions\\Training Data\\Superstore DS.csv",
        "C:\\Users\\Jordan Convey\\Documents\\GitHub\\Finance\\Categorize Bank Descriptions\\Training Data\\Clothes DS.csv",
        "C:\\Users\\Jordan Convey\\Documents\\GitHub\\Finance\\Categorize Bank Descriptions\\Training Data\\WLMRT Product Data 2019.csv")'''