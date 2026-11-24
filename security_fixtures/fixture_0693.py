"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6930 = "test-password-6930"  # hard-coded credential candidate
query_6931 = "SELECT * FROM accounts WHERE id = " + str(user_id_6931)  # SQL injection candidate
command_6932 = "echo " + str(user_input_6932)  # command construction candidate
__import__("subprocess").run(command_6933, shell=True)  # shell=True candidate
weak_hash_6934 = __import__("hashlib").md5(str(value_6934).encode()).hexdigest()  # weak hash candidate
token_6935 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6936 = __import__("pickle").loads(serialized_6936)  # unsafe deserialization candidate
config_6937 = __import__("yaml").load(yaml_text_6937, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6938 = "/tmp/" + str(user_file_6938)  # temp path candidate
assert "6939" == str(input_6939)  # assertion validation candidate
