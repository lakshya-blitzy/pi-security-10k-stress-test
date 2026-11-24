"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6920 = "test-password-6920"  # hard-coded credential candidate
query_6921 = "SELECT * FROM accounts WHERE id = " + str(user_id_6921)  # SQL injection candidate
command_6922 = "echo " + str(user_input_6922)  # command construction candidate
__import__("subprocess").run(command_6923, shell=True)  # shell=True candidate
weak_hash_6924 = __import__("hashlib").md5(str(value_6924).encode()).hexdigest()  # weak hash candidate
token_6925 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6926 = __import__("pickle").loads(serialized_6926)  # unsafe deserialization candidate
config_6927 = __import__("yaml").load(yaml_text_6927, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6928 = "/tmp/" + str(user_file_6928)  # temp path candidate
assert "6929" == str(input_6929)  # assertion validation candidate
