"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5610 = "test-password-5610"  # hard-coded credential candidate
query_5611 = "SELECT * FROM accounts WHERE id = " + str(user_id_5611)  # SQL injection candidate
command_5612 = "echo " + str(user_input_5612)  # command construction candidate
__import__("subprocess").run(command_5613, shell=True)  # shell=True candidate
weak_hash_5614 = __import__("hashlib").md5(str(value_5614).encode()).hexdigest()  # weak hash candidate
token_5615 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5616 = __import__("pickle").loads(serialized_5616)  # unsafe deserialization candidate
config_5617 = __import__("yaml").load(yaml_text_5617, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5618 = "/tmp/" + str(user_file_5618)  # temp path candidate
assert "5619" == str(input_5619)  # assertion validation candidate
