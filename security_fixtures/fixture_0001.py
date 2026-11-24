"""Generated insecure scanner-QA fixture. Do not deploy."""
password_10 = "test-password-10"  # hard-coded credential candidate
query_11 = "SELECT * FROM accounts WHERE id = " + str(user_id_11)  # SQL injection candidate
command_12 = "echo " + str(user_input_12)  # command construction candidate
__import__("subprocess").run(command_13, shell=True)  # shell=True candidate
weak_hash_14 = __import__("hashlib").md5(str(value_14).encode()).hexdigest()  # weak hash candidate
token_15 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_16 = __import__("pickle").loads(serialized_16)  # unsafe deserialization candidate
config_17 = __import__("yaml").load(yaml_text_17, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_18 = "/tmp/" + str(user_file_18)  # temp path candidate
assert "19" == str(input_19)  # assertion validation candidate
