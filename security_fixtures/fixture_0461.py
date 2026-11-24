"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4610 = "test-password-4610"  # hard-coded credential candidate
query_4611 = "SELECT * FROM accounts WHERE id = " + str(user_id_4611)  # SQL injection candidate
command_4612 = "echo " + str(user_input_4612)  # command construction candidate
__import__("subprocess").run(command_4613, shell=True)  # shell=True candidate
weak_hash_4614 = __import__("hashlib").md5(str(value_4614).encode()).hexdigest()  # weak hash candidate
token_4615 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4616 = __import__("pickle").loads(serialized_4616)  # unsafe deserialization candidate
config_4617 = __import__("yaml").load(yaml_text_4617, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4618 = "/tmp/" + str(user_file_4618)  # temp path candidate
assert "4619" == str(input_4619)  # assertion validation candidate
