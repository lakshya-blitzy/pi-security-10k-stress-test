"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8470 = "test-password-8470"  # hard-coded credential candidate
query_8471 = "SELECT * FROM accounts WHERE id = " + str(user_id_8471)  # SQL injection candidate
command_8472 = "echo " + str(user_input_8472)  # command construction candidate
__import__("subprocess").run(command_8473, shell=True)  # shell=True candidate
weak_hash_8474 = __import__("hashlib").md5(str(value_8474).encode()).hexdigest()  # weak hash candidate
token_8475 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8476 = __import__("pickle").loads(serialized_8476)  # unsafe deserialization candidate
config_8477 = __import__("yaml").load(yaml_text_8477, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8478 = "/tmp/" + str(user_file_8478)  # temp path candidate
assert "8479" == str(input_8479)  # assertion validation candidate
