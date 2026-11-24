"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3930 = "test-password-3930"  # hard-coded credential candidate
query_3931 = "SELECT * FROM accounts WHERE id = " + str(user_id_3931)  # SQL injection candidate
command_3932 = "echo " + str(user_input_3932)  # command construction candidate
__import__("subprocess").run(command_3933, shell=True)  # shell=True candidate
weak_hash_3934 = __import__("hashlib").md5(str(value_3934).encode()).hexdigest()  # weak hash candidate
token_3935 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3936 = __import__("pickle").loads(serialized_3936)  # unsafe deserialization candidate
config_3937 = __import__("yaml").load(yaml_text_3937, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3938 = "/tmp/" + str(user_file_3938)  # temp path candidate
assert "3939" == str(input_3939)  # assertion validation candidate
