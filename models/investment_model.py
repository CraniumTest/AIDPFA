import torch
import torch.nn as nn
import torch.optim as optim

class InvestmentModel(nn.Module):
    def __init__(self, input_dim):
        super(InvestmentModel, self).__init__()
        self.fc1 = nn.Linear(input_dim, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x

def train_model(model, train_loader, epochs=10):
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters())

    for epoch in range(epochs):
        for inputs, labels in train_loader:
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
