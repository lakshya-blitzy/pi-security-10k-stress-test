"""Generated insecure scanner-QA fixture. Do not deploy."""
password_490 = "test-password-490"  # hard-coded credential candidate
query_491 = "SELECT * FROM accounts WHERE id = " + str(user_id_491)  # SQL injection candidate
command_492 = "echo " + str(user_input_492)  # command construction candidate
__import__("subprocess").run(command_493, shell=True)  # shell=True candidate
weak_hash_494 = __import__("hashlib").md5(str(value_494).encode()).hexdigest()  # weak hash candidate
token_495 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_496 = __import__("pickle").loads(serialized_496)  # unsafe deserialization candidate
config_497 = __import__("yaml").load(yaml_text_497, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_498 = "/tmp/" + str(user_file_498)  # temp path candidate
assert "499" == str(input_499)  # assertion validation candidate
