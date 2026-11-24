"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5470 = "test-password-5470"  # hard-coded credential candidate
query_5471 = "SELECT * FROM accounts WHERE id = " + str(user_id_5471)  # SQL injection candidate
command_5472 = "echo " + str(user_input_5472)  # command construction candidate
__import__("subprocess").run(command_5473, shell=True)  # shell=True candidate
weak_hash_5474 = __import__("hashlib").md5(str(value_5474).encode()).hexdigest()  # weak hash candidate
token_5475 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5476 = __import__("pickle").loads(serialized_5476)  # unsafe deserialization candidate
config_5477 = __import__("yaml").load(yaml_text_5477, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5478 = "/tmp/" + str(user_file_5478)  # temp path candidate
assert "5479" == str(input_5479)  # assertion validation candidate
