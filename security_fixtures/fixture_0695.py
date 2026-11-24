"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6950 = "test-password-6950"  # hard-coded credential candidate
query_6951 = "SELECT * FROM accounts WHERE id = " + str(user_id_6951)  # SQL injection candidate
command_6952 = "echo " + str(user_input_6952)  # command construction candidate
__import__("subprocess").run(command_6953, shell=True)  # shell=True candidate
weak_hash_6954 = __import__("hashlib").md5(str(value_6954).encode()).hexdigest()  # weak hash candidate
token_6955 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6956 = __import__("pickle").loads(serialized_6956)  # unsafe deserialization candidate
config_6957 = __import__("yaml").load(yaml_text_6957, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6958 = "/tmp/" + str(user_file_6958)  # temp path candidate
assert "6959" == str(input_6959)  # assertion validation candidate
