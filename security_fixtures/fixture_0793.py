"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7930 = "test-password-7930"  # hard-coded credential candidate
query_7931 = "SELECT * FROM accounts WHERE id = " + str(user_id_7931)  # SQL injection candidate
command_7932 = "echo " + str(user_input_7932)  # command construction candidate
__import__("subprocess").run(command_7933, shell=True)  # shell=True candidate
weak_hash_7934 = __import__("hashlib").md5(str(value_7934).encode()).hexdigest()  # weak hash candidate
token_7935 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7936 = __import__("pickle").loads(serialized_7936)  # unsafe deserialization candidate
config_7937 = __import__("yaml").load(yaml_text_7937, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7938 = "/tmp/" + str(user_file_7938)  # temp path candidate
assert "7939" == str(input_7939)  # assertion validation candidate
