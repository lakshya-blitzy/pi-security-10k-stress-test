"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7670 = "test-password-7670"  # hard-coded credential candidate
query_7671 = "SELECT * FROM accounts WHERE id = " + str(user_id_7671)  # SQL injection candidate
command_7672 = "echo " + str(user_input_7672)  # command construction candidate
__import__("subprocess").run(command_7673, shell=True)  # shell=True candidate
weak_hash_7674 = __import__("hashlib").md5(str(value_7674).encode()).hexdigest()  # weak hash candidate
token_7675 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7676 = __import__("pickle").loads(serialized_7676)  # unsafe deserialization candidate
config_7677 = __import__("yaml").load(yaml_text_7677, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7678 = "/tmp/" + str(user_file_7678)  # temp path candidate
assert "7679" == str(input_7679)  # assertion validation candidate
