.PHONY: help install dev-install clean lint format test security run build package

# Default target
help:
	@echo "RefiX - Development Commands"
	@echo "============================"
	@echo "install       - Install production dependencies"
	@echo "dev-install   - Install development dependencies"
	@echo "clean         - Remove build artifacts and cache files"
	@echo "lint          - Run code quality checks (flake8, pylint)"
	@echo "format        - Format code with black"
	@echo "type-check    - Run type checking with mypy"
	@echo "security      - Run security checks (bandit, safety)"
	@echo "test          - Run tests (if available)"
	@echo "run           - Run the application"
	@echo "build         - Build distribution packages"
	@echo "package       - Create distributable package"

# Install production dependencies
install:
	pip install -r requirements.txt

# Install development dependencies
dev-install:
	pip install -r requirements.txt
	pip install flake8 pylint black mypy bandit safety pytest pytest-cov

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	find . -type d -name '*.egg-info' -exec rm -rf {} +
	rm -rf build dist .pytest_cache .mypy_cache .coverage htmlcov
	rm -f *.log bandit-report.json
	@echo "Clean complete!"

# Run linters
lint:
	@echo "Running flake8..."
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics || true
	flake8 . --count --max-complexity=10 --max-line-length=100 --statistics || true
	@echo "\nRunning pylint..."
	pylint APP.py gemini gui --rcfile=.pylintrc || true

# Format code
format:
	@echo "Formatting code with black..."
	black --line-length=100 .
	@echo "Format complete!"

# Type checking
type-check:
	@echo "Running mypy type checker..."
	mypy --ignore-missing-imports . || true

# Security checks
security:
	@echo "Running security checks..."
	@echo "\n=== Bandit Security Scan ==="
	bandit -r . -f screen || true
	@echo "\n=== Safety Dependency Check ==="
	safety check || true

# Run tests
test:
	@echo "Running tests..."
	@if [ -d "tests" ]; then \
		pytest tests/ -v --cov=. --cov-report=html --cov-report=term; \
	else \
		echo "No tests directory found. Skipping tests."; \
	fi

# Run the application
run:
	python APP.py

# Build distribution packages
build: clean
	@echo "Building distribution packages..."
	python -m build

# Create package
package: clean
	@echo "Creating distributable package..."
	python setup.py sdist bdist_wheel
	@echo "Package created in dist/"

# Validate all
validate: clean lint type-check security
	@echo "\n✅ Validation complete!"
