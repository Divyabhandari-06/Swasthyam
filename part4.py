# Import necessary libraries
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Load and preprocess dataset
# Assuming dataset has columns: 'age', 'gender', 'health_concerns', 'yoga_level', 'custom_yoga_plan'
data = pd.read_csv('health_data.csv')
X = data[['age', 'gender', 'health_concerns', 'yoga_level']]  # Input features
y = data['custom_yoga_plan']  # Target

# Encode categorical variables (e.g., gender and health concerns)
X = pd.get_dummies(X, columns=['gender', 'health_concerns'])

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
Dense(1, activation='sigmoid')  # Assuming binary output for yoga plan
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20, batch_size=32)

# Evaluate the model
accuracy = model.evaluate(X_test, y_test)[1]
print(f"Model Accuracy: {accuracy:.2f}")

# Save the model for future use
model.save('yoga_plan_model.h5')

# Predict customized yoga plans (example input)
example_data = [[30, 'Male', 'Back Pain', 'Intermediate']]  # Replace with real data
example_data = pd.get_dummies(pd.DataFrame(example_data, columns=['age', 'gender', 'health_concerns', 'yoga_level']))
example_data = scaler.transform(example_data)
prediction = model.predict(example_data)
print(f"Predicted yoga plan: {prediction}")