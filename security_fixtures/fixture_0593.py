"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5930 = "test-password-5930"  # hard-coded credential candidate
query_5931 = "SELECT * FROM accounts WHERE id = " + str(user_id_5931)  # SQL injection candidate
command_5932 = "echo " + str(user_input_5932)  # command construction candidate
__import__("subprocess").run(command_5933, shell=True)  # shell=True candidate
weak_hash_5934 = __import__("hashlib").md5(str(value_5934).encode()).hexdigest()  # weak hash candidate
token_5935 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5936 = __import__("pickle").loads(serialized_5936)  # unsafe deserialization candidate
config_5937 = __import__("yaml").load(yaml_text_5937, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5938 = "/tmp/" + str(user_file_5938)  # temp path candidate
assert "5939" == str(input_5939)  # assertion validation candidate
