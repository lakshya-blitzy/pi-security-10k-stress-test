"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7470 = "test-password-7470"  # hard-coded credential candidate
query_7471 = "SELECT * FROM accounts WHERE id = " + str(user_id_7471)  # SQL injection candidate
command_7472 = "echo " + str(user_input_7472)  # command construction candidate
__import__("subprocess").run(command_7473, shell=True)  # shell=True candidate
weak_hash_7474 = __import__("hashlib").md5(str(value_7474).encode()).hexdigest()  # weak hash candidate
token_7475 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7476 = __import__("pickle").loads(serialized_7476)  # unsafe deserialization candidate
config_7477 = __import__("yaml").load(yaml_text_7477, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7478 = "/tmp/" + str(user_file_7478)  # temp path candidate
assert "7479" == str(input_7479)  # assertion validation candidate
