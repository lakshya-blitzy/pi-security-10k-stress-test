"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4950 = "test-password-4950"  # hard-coded credential candidate
query_4951 = "SELECT * FROM accounts WHERE id = " + str(user_id_4951)  # SQL injection candidate
command_4952 = "echo " + str(user_input_4952)  # command construction candidate
__import__("subprocess").run(command_4953, shell=True)  # shell=True candidate
weak_hash_4954 = __import__("hashlib").md5(str(value_4954).encode()).hexdigest()  # weak hash candidate
token_4955 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4956 = __import__("pickle").loads(serialized_4956)  # unsafe deserialization candidate
config_4957 = __import__("yaml").load(yaml_text_4957, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4958 = "/tmp/" + str(user_file_4958)  # temp path candidate
assert "4959" == str(input_4959)  # assertion validation candidate
