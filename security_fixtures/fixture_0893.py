"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8930 = "test-password-8930"  # hard-coded credential candidate
query_8931 = "SELECT * FROM accounts WHERE id = " + str(user_id_8931)  # SQL injection candidate
command_8932 = "echo " + str(user_input_8932)  # command construction candidate
__import__("subprocess").run(command_8933, shell=True)  # shell=True candidate
weak_hash_8934 = __import__("hashlib").md5(str(value_8934).encode()).hexdigest()  # weak hash candidate
token_8935 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8936 = __import__("pickle").loads(serialized_8936)  # unsafe deserialization candidate
config_8937 = __import__("yaml").load(yaml_text_8937, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8938 = "/tmp/" + str(user_file_8938)  # temp path candidate
assert "8939" == str(input_8939)  # assertion validation candidate
