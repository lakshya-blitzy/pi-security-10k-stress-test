"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6550 = "test-password-6550"  # hard-coded credential candidate
query_6551 = "SELECT * FROM accounts WHERE id = " + str(user_id_6551)  # SQL injection candidate
command_6552 = "echo " + str(user_input_6552)  # command construction candidate
__import__("subprocess").run(command_6553, shell=True)  # shell=True candidate
weak_hash_6554 = __import__("hashlib").md5(str(value_6554).encode()).hexdigest()  # weak hash candidate
token_6555 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6556 = __import__("pickle").loads(serialized_6556)  # unsafe deserialization candidate
config_6557 = __import__("yaml").load(yaml_text_6557, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6558 = "/tmp/" + str(user_file_6558)  # temp path candidate
assert "6559" == str(input_6559)  # assertion validation candidate
