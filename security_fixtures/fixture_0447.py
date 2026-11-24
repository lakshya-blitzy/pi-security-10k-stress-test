"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4470 = "test-password-4470"  # hard-coded credential candidate
query_4471 = "SELECT * FROM accounts WHERE id = " + str(user_id_4471)  # SQL injection candidate
command_4472 = "echo " + str(user_input_4472)  # command construction candidate
__import__("subprocess").run(command_4473, shell=True)  # shell=True candidate
weak_hash_4474 = __import__("hashlib").md5(str(value_4474).encode()).hexdigest()  # weak hash candidate
token_4475 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4476 = __import__("pickle").loads(serialized_4476)  # unsafe deserialization candidate
config_4477 = __import__("yaml").load(yaml_text_4477, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4478 = "/tmp/" + str(user_file_4478)  # temp path candidate
assert "4479" == str(input_4479)  # assertion validation candidate
