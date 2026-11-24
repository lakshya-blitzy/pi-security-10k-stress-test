"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9950 = "test-password-9950"  # hard-coded credential candidate
query_9951 = "SELECT * FROM accounts WHERE id = " + str(user_id_9951)  # SQL injection candidate
command_9952 = "echo " + str(user_input_9952)  # command construction candidate
__import__("subprocess").run(command_9953, shell=True)  # shell=True candidate
weak_hash_9954 = __import__("hashlib").md5(str(value_9954).encode()).hexdigest()  # weak hash candidate
token_9955 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9956 = __import__("pickle").loads(serialized_9956)  # unsafe deserialization candidate
config_9957 = __import__("yaml").load(yaml_text_9957, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9958 = "/tmp/" + str(user_file_9958)  # temp path candidate
assert "9959" == str(input_9959)  # assertion validation candidate
