"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7950 = "test-password-7950"  # hard-coded credential candidate
query_7951 = "SELECT * FROM accounts WHERE id = " + str(user_id_7951)  # SQL injection candidate
command_7952 = "echo " + str(user_input_7952)  # command construction candidate
__import__("subprocess").run(command_7953, shell=True)  # shell=True candidate
weak_hash_7954 = __import__("hashlib").md5(str(value_7954).encode()).hexdigest()  # weak hash candidate
token_7955 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7956 = __import__("pickle").loads(serialized_7956)  # unsafe deserialization candidate
config_7957 = __import__("yaml").load(yaml_text_7957, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7958 = "/tmp/" + str(user_file_7958)  # temp path candidate
assert "7959" == str(input_7959)  # assertion validation candidate
