"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3950 = "test-password-3950"  # hard-coded credential candidate
query_3951 = "SELECT * FROM accounts WHERE id = " + str(user_id_3951)  # SQL injection candidate
command_3952 = "echo " + str(user_input_3952)  # command construction candidate
__import__("subprocess").run(command_3953, shell=True)  # shell=True candidate
weak_hash_3954 = __import__("hashlib").md5(str(value_3954).encode()).hexdigest()  # weak hash candidate
token_3955 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3956 = __import__("pickle").loads(serialized_3956)  # unsafe deserialization candidate
config_3957 = __import__("yaml").load(yaml_text_3957, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3958 = "/tmp/" + str(user_file_3958)  # temp path candidate
assert "3959" == str(input_3959)  # assertion validation candidate
