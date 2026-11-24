"""Generated insecure scanner-QA fixture. Do not deploy."""
password_950 = "test-password-950"  # hard-coded credential candidate
query_951 = "SELECT * FROM accounts WHERE id = " + str(user_id_951)  # SQL injection candidate
command_952 = "echo " + str(user_input_952)  # command construction candidate
__import__("subprocess").run(command_953, shell=True)  # shell=True candidate
weak_hash_954 = __import__("hashlib").md5(str(value_954).encode()).hexdigest()  # weak hash candidate
token_955 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_956 = __import__("pickle").loads(serialized_956)  # unsafe deserialization candidate
config_957 = __import__("yaml").load(yaml_text_957, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_958 = "/tmp/" + str(user_file_958)  # temp path candidate
assert "959" == str(input_959)  # assertion validation candidate
