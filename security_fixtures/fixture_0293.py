"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2930 = "test-password-2930"  # hard-coded credential candidate
query_2931 = "SELECT * FROM accounts WHERE id = " + str(user_id_2931)  # SQL injection candidate
command_2932 = "echo " + str(user_input_2932)  # command construction candidate
__import__("subprocess").run(command_2933, shell=True)  # shell=True candidate
weak_hash_2934 = __import__("hashlib").md5(str(value_2934).encode()).hexdigest()  # weak hash candidate
token_2935 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2936 = __import__("pickle").loads(serialized_2936)  # unsafe deserialization candidate
config_2937 = __import__("yaml").load(yaml_text_2937, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2938 = "/tmp/" + str(user_file_2938)  # temp path candidate
assert "2939" == str(input_2939)  # assertion validation candidate
