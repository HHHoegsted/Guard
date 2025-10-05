"""
	This class module implements guards in Python. 
	
	Why use guards?

	Guards are a simple and explicit way to enforce assumptions about input values.
	They make code safer, more predictable, and easier to reason about by validating
	arguments before they are used.

	In most cases, unexpected behavior in a system comes not from the logic itself,
	but from invalid data entering that logic. Guard clauses act as early warning
	systems — they stop the program immediately when inputs don’t meet expectations,
	making the source of the problem obvious and easier to debug.

	Using guards provides several benefits:
	- **Fail fast:** Detect errors at the point of entry instead of letting them
	propagate through the system.
	- **Improve readability:** Validation expressed as `Guard.against_null(x)`
	clearly communicates intent.
	- **Reduce repetition:** Common validation patterns can be reused consistently
	across the codebase.
	- **Enhance robustness:** Protects code from subtle or hard-to-trace runtime errors.
	- **Encourage good design:** Explicitly documenting preconditions leads to more
	maintainable and self-explanatory code.

	In short, guards make defensive programming elegant — turning what would otherwise
	be scattered `if` statements into a clear, reusable validation layer.
"""

import os
from typing import Any
from numbers import Number
from collections.abc import Iterable


class Guard():
	"""
		A utility class providing static guard methods for validating function arguments.

		The `Guard` class is designed to make argument validation concise and expressive,
		preventing invalid or unexpected values early in code execution. Each method raises
		an appropriate Python exception (such as `ValueError`, `TypeError`, or
		`FileNotFoundError`) when validation fails, and returns the validated argument
		otherwise. This allows guards to be used inline in assignments or function calls.

		Example:
			>>> from guard import Guard
			>>> value = Guard.against_none(input_value, "input_value")
			>>> count = Guard.against_negative(user_count, "user_count")
	"""

	@staticmethod
	def against_none(argument: Any, argument_name: str = "value"):
		"""
		Raises an exception if the given argument is None.

		This guard ensures that a required argument has been provided and is not `None`.
		It is useful for enforcing non-null preconditions before performing operations
		that assume the presence of a valid object or value.

		Args:
			argument (Any): The value to check.
			argument_name (str, optional): The name of the argument being validated.
				Used in the error message for clarity. Defaults to "value".

		Raises:
			ValueError: If `argument` is None.

		Returns:
			Any: The original argument, unchanged, if validation passes.
		"""

		if argument is None:
			raise ValueError(f"Argument '{argument_name}' must not be None.")
		return argument
	
	@staticmethod
	def against_negative(argument: Number, argument_name: str = "value"):
		"""
		Raises an exception if the given numeric argument is negative.

		This guard ensures that a numeric value is zero or positive, preventing the use
		of invalid negative numbers in contexts such as counts, sizes, or other quantities
		that must not be less than zero.

		Args:
			argument (Number): The numeric value to check.
			argument_name (str, optional): The name of the argument being validated.
				Used in the error message for clarity. Defaults to "value".

		Raises:
			ValueError: If `argument` is less than zero.

		Returns:
			Number: The original argument, unchanged, if validation passes.
		"""

		if argument < 0:
			raise ValueError(f"Argument '{argument_name}' must be positive")
		return argument
	
	@staticmethod
	def against_empty_string(argument: str, argument_name: str = "value"):
		"""
		Raises an exception if the given string argument is empty.

		This guard ensures that a string value contains at least one character.
		It is useful for validating identifiers, names, or any required text input
		that must not be an empty string.

		Args:
			argument (str): The string value to check.
			argument_name (str, optional): The name of the argument being validated.
				Used in the error message for clarity. Defaults to "value".

		Raises:
			ValueError: If `argument` is an empty string.

		Returns:
			str: The original argument, unchanged, if validation passes.
		"""
		if argument == "":
			raise ValueError (f"Argument '{argument_name}' must not be ''")
		return argument
	
	@staticmethod
	def against_zero(argument: Number, argument_name: str = "value"):
		"""
		Raises an exception if the given numeric argument is zero.

		This guard is useful in contexts where zero is not a valid value,
		such as when used as a divisor, a scaling factor, or an identifier
		that must be nonzero.

		Args:
			argument (Number): The numeric value to check.
			argument_name (str, optional): The name of the argument being validated.
				Used in the error message for clarity. Defaults to "value".

		Raises:
			ValueError: If `argument` equals zero.

		Returns:
			Number: The original argument, unchanged, if validation passes.
		"""
		if argument == 0:
			raise ValueError(f"Argument '{argument_name}' must not be zero.")
		return argument

	@staticmethod
	def against_empty_collection(argument, argument_name: str = "value"):
		"""
		Raises an exception if the given collection is empty.

		This guard ensures that an iterable or collection (such as a list, tuple,
		set, or dictionary) contains at least one element. It is useful for validating
		inputs where an empty container would make further processing invalid or meaningless.

		Args:
			argument (Any): The collection or iterable to check.
			argument_name (str, optional): The name of the argument being validated.
				Used in the error message for clarity. Defaults to "value".

		Raises:
			ValueError: If `argument` is empty or evaluates to False.

		Returns:
			Any: The original argument, unchanged, if validation passes.
		"""
		if not argument:
			raise ValueError(f"Argument '{argument_name}' must not be empty.")
		return argument
	
	@staticmethod
	def against_wrong_type(argument: Any, expected_type: type, argument_name: str = "value"):
		"""
		Raises an exception if the given argument is not of the expected type.

		This guard validates that an argument matches the required type before it is used.
		It helps catch programming errors early, especially in dynamically typed code where
		type assumptions might otherwise go unchecked.

		Args:
			argument (Any): The value to check.
			expected_type (type): The expected type or class the argument should be an instance of.
			argument_name (str, optional): The name of the argument being validated.
				Used in the error message for clarity. Defaults to "value".

		Raises:
			TypeError: If `argument` is not an instance of `expected_type`.

		Returns:
			Any: The original argument, unchanged, if validation passes.
		"""
		if not isinstance(argument, expected_type):
			raise TypeError(f"Argument '{argument_name}' must be of type {expected_type.__name__}. Got {type(argument).__name__}.")
		return argument

	@staticmethod
	def against_file_not_found(path: Any, argument_name: str = "file_path"):
		"""
		Raises an exception if the specified file path does not exist.

		This guard validates that the given path points to an existing file.
		It helps ensure that file-dependent operations do not fail unexpectedly
		due to missing or invalid file paths.

		Args:
			path (Any): The file path to check. Must be a valid `str`, `bytes`,
				or `os.PathLike` object.
			argument_name (str, optional): The name of the argument being validated.
				Used in the error message for clarity. Defaults to "file_path".

		Raises:
			ValueError: If `path` is None.
			TypeError: If `path` is not a valid path-like type.
			FileNotFoundError: If the file does not exist at the given path.

		Returns:
			Any: The original path, unchanged, if validation passes.
		"""
		if path is None:
			raise ValueError(f"Argument '{argument_name}' must not be None.")
		if not isinstance(path, (str, bytes, os.PathLike)):
			raise TypeError(f"Argument '{argument_name}' must be a valid file path (str, bytes, or os.PathLike).")
		if not os.path.exists(path):
			raise FileNotFoundError(f"File not found: '{path}'")
		return path
	
	@staticmethod
	def against_directory_not_found(path: Any, argument_name: str = "directory"):
		"""
		Raises an exception if the specified directory path does not exist.

		This guard ensures that a given path points to a valid, existing directory.
		It is useful for validating configuration paths, output locations, or any
		file system directories required by the program.

		Args:
			path (Any): The directory path to check. Must be a valid `str`, `bytes`,
				or `os.PathLike` object.
			argument_name (str, optional): The name of the argument being validated.
				Used in the error message for clarity. Defaults to "directory".

		Raises:
			FileNotFoundError: If the specified directory does not exist.

		Returns:
			Any: The original path, unchanged, if validation passes.
		"""
		if not os.path.isdir(path):
			raise FileNotFoundError(f"Directory not found: '{path}'")
		return path
	
	@staticmethod
	def against_not_iterable(argument: Any, argument_name: str = "value"):
		"""
		Raises an exception if the given argument is not an iterable.

		This guard ensures that the provided argument supports iteration, such as lists,
		tuples, sets, or generators, while explicitly excluding `str` and `bytes`, which
		are technically iterable but often represent single values rather than collections.

		Args:
			argument (Any): The value to check for iterability.
			argument_name (str, optional): The name of the argument being validated.
				Used in the error message for clarity. Defaults to "value".

		Raises:
			TypeError: If `argument` is not iterable or is a `str`/`bytes` instance.

		Returns:
			Any: The original argument, unchanged, if validation passes.
		"""
		if not isinstance(argument, Iterable) or isinstance(argument, (str, bytes)):
			raise TypeError(f"Argument '{argument_name}' must be an iterable (not str/bytes).")
		return argument

