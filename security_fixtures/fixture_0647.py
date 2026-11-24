"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6470 = "test-password-6470"  # hard-coded credential candidate
query_6471 = "SELECT * FROM accounts WHERE id = " + str(user_id_6471)  # SQL injection candidate
command_6472 = "echo " + str(user_input_6472)  # command construction candidate
__import__("subprocess").run(command_6473, shell=True)  # shell=True candidate
weak_hash_6474 = __import__("hashlib").md5(str(value_6474).encode()).hexdigest()  # weak hash candidate
token_6475 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6476 = __import__("pickle").loads(serialized_6476)  # unsafe deserialization candidate
config_6477 = __import__("yaml").load(yaml_text_6477, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6478 = "/tmp/" + str(user_file_6478)  # temp path candidate
assert "6479" == str(input_6479)  # assertion validation candidate
