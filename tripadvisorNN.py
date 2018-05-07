
import tensorflow as tf

feature_names = ['Usercountry', 'Nrreviews','Nrhotelreviews','Helpfulvotes','Score','Periodofstay',
           'Travelertype','Pool','Gym','Tenniscourt','Spa','Casino','Freeinternet',
                  'Hotelname','Hotelstars','Nrrooms','Usercontinent','Memberyears',
           'Reviewmonth','Reviewweekday']
FIELD_DEFAULTS = [[0], [0], [0], [0], [0],
                  [0], [0], [0], [0], [0],
                  [0], [0], [0], [0], [0],
                  [0], [0], [0], [0], [0]]

def parse_line(line):
    parsed_line = tf.decode_csv(line, FIELD_DEFAULTS)
    label = parsed_line[4]
    del parsed_line[4]
    features = parsed_line  
    d = dict(zip(feature_names, features))
    print ("dictionary", d, " label = ", label)    
    return d, label

def csv_input_fn(csv_path, batch_size):
    dataset = tf.data.TextLineDataset(csv_path)
    dataset = dataset.map(parse_line)
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)
    return dataset

Usercountry = tf.feature_column.indicator_column(tf.feature_column.categorical_column_with_identity("Usercountry",47))

Nrreviews = tf.feature_column.numeric_column("Nrreviews")

Nrhotelreviews = tf.feature_column.numeric_column("Nrhotelreviews")

Helpfulvotes = tf.feature_column.numeric_column("Helpfulvotes")

Periodofstay = tf.feature_column.numeric_column("Periodofstay")

Travelertype = tf.feature_column.indicator_column(tf.feature_column.categorical_column_with_identity("Travelertype",5))

Pool = tf.feature_column.indicator_column(tf.feature_column.categorical_column_with_identity("Pool",2))

Gym = tf.feature_column.indicator_column(tf.feature_column.categorical_column_with_identity("Gym",2))

Tenniscourt = tf.feature_column.indicator_column(tf.feature_column.categorical_column_with_identity("Tenniscourt",2))

Spa = tf.feature_column.indicator_column(tf.feature_column.categorical_column_with_identity("Spa",2))

Casino = tf.feature_column.indicator_column(tf.feature_column.categorical_column_with_identity("Casino",2))

Freeinternet = tf.feature_column.indicator_column(tf.feature_column.categorical_column_with_identity("Freeinternet",2))

Hotelname = tf.feature_column.indicator_column(tf.feature_column.categorical_column_with_identity("Hotelname",24))

Hotelstars = tf.feature_column.indicator_column(tf.feature_column.categorical_column_with_identity("Hotelstars",5))

Nrrooms = tf.feature_column.numeric_column("Nrrooms")

Usercontinent = tf.feature_column.indicator_column(tf.feature_column.categorical_column_with_identity("Usercontinent",6))

Memberyears = tf.feature_column.numeric_column("Memberyears")

Reviewmonth = tf.feature_column.indicator_column(tf.feature_column.categorical_column_with_identity("Reviewmonth",12))

Reviewweekday = tf.feature_column.indicator_column(tf.feature_column.categorical_column_with_identity("Reviewweekday",7))

feature_columns = [Usercountry, Nrreviews,Nrhotelreviews,Helpfulvotes,Periodofstay,
         Travelertype,Pool,Gym,Tenniscourt,Spa,Casino,Freeinternet,Hotelname,Hotelstars,Nrrooms,Usercontinent,Memberyears,Reviewmonth,Reviewweekday]

classifier=tf.estimator.DNNClassifier(
    feature_columns=feature_columns,  
    hidden_units=[10, 10], 
    n_classes=5,
    model_dir="/tmp")

batch_size = 100

classifier.train(
    steps=1000,
    input_fn=lambda : csv_input_fn("/home/walker/tripAdvisorFL.csv", batch_size))
