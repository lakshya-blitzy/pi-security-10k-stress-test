"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7920 = "test-password-7920"  # hard-coded credential candidate
query_7921 = "SELECT * FROM accounts WHERE id = " + str(user_id_7921)  # SQL injection candidate
command_7922 = "echo " + str(user_input_7922)  # command construction candidate
__import__("subprocess").run(command_7923, shell=True)  # shell=True candidate
weak_hash_7924 = __import__("hashlib").md5(str(value_7924).encode()).hexdigest()  # weak hash candidate
token_7925 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7926 = __import__("pickle").loads(serialized_7926)  # unsafe deserialization candidate
config_7927 = __import__("yaml").load(yaml_text_7927, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7928 = "/tmp/" + str(user_file_7928)  # temp path candidate
assert "7929" == str(input_7929)  # assertion validation candidate
