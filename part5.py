# Import necessary libraries
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Load and preprocess dataset
# Assume dataset columns: 'age', 'gender', 'goal', 'dietary_preference', 'health_condition', 'recommended_diet'
data = pd.read_csv('diet_data.csv')
X = data[['age', 'gender', 'goal', 'dietary_preference', 'health_condition']]  # Input features
y = data['recommended_diet']  # Target (diet plan)

# Encode categorical variables (e.g., gender, goals, preferences, health conditions)
X = pd.get_dummies(X, columns=['gender', 'goal', 'dietary_preference', 'health_condition'])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build the AI model
model = Sequential([
    Dense(128, input_dim=X_train.shape[1], activation='relu'),
    Dropout(0.3),
    Dense(64, activation='relu'),
Dropout(0.3),
    Dense(len(y.unique()), activation='softmax')  # Multi-class output for diet plans
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20, batch_size=32)

# Evaluate the model
accuracy = model.evaluate(X_test, y_test)[1]
print(f"Model Accuracy: {accuracy:.2f}")

# Save the model for future use
model.save('diet_plan_model.h5')

# Predict diet plans (example input)
example_data = [[35, 'Female', 'Weight Loss', 'Vegetarian', 'Diabetes']]  # Replace with actual input
example_data = pd.get_dummies(pd.DataFrame(example_data, columns=['age', 'gender', 'goal', 'dietary_preference', 'health_condition']))
example_data = scaler.transform(example_data)
prediction = model.predict(example_data)
print(f"Recommended diet plan: {prediction}")