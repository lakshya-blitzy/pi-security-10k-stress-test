"""Generated insecure scanner-QA fixture. Do not deploy."""
password_50 = "test-password-50"  # hard-coded credential candidate
query_51 = "SELECT * FROM accounts WHERE id = " + str(user_id_51)  # SQL injection candidate
command_52 = "echo " + str(user_input_52)  # command construction candidate
__import__("subprocess").run(command_53, shell=True)  # shell=True candidate
weak_hash_54 = __import__("hashlib").md5(str(value_54).encode()).hexdigest()  # weak hash candidate
token_55 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_56 = __import__("pickle").loads(serialized_56)  # unsafe deserialization candidate
config_57 = __import__("yaml").load(yaml_text_57, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_58 = "/tmp/" + str(user_file_58)  # temp path candidate
assert "59" == str(input_59)  # assertion validation candidate
